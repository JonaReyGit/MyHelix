'use client'

import { useState } from 'react'
import {createClient} from '@/lib/supabase/client'
import { useRef } from "react"

export default function UploadPage() {
    const [status, setStatus] = useState<string>('')
    const supabase = createClient()

    async function handleUpload(e: React.ChangeEvent<HTMLInputElement>) {
        const file = e.target.files?.[0]
        if (!file) return

        setStatus('Uploading...')

        const { data: { user } } = await supabase.auth.getUser()
        if (!user) {
            setStatus('Please log in first')
            return
        }

        const filePath = '${user.id}/${Date.now()}_${file.name}'

        const { error: uploadError } = await supabase.storage
        .from('genetic-uploads')
        .upload(filePath, file)

        if (uploadError) {
            setStatus('Upload failed: ${uploadError.message}')
            return
        }

        const { error: dbError } = await supabase.from('uploads').insert({
            user_id: user.id,
            file_name: file.name,
            file_path: filePath,
            status: 'pending'
        })

        if (dbError){
            setStatus('Saved file but failed to save metadata ${dbError.message}')
            return
        }

        setStatus('Upload complete - processing will begin shortly')

        
    }
    
    return (

        <div className="min-h-screen flex items-center justify-center p-6">
            <label className="w-full max-w-md flex flex-col items-center justify-center gap-2 p-8 border-2 border-dashed border-gray-300 rounded-lg cursor-pointer hover:border-blue-400 hover:bg-blue-50 transition-colors">
                <span className="text-lg font-bold text-gray-600">
                Click to upload your genetic data file
                </span>
                <span className="text-xs text-gray-400">.txt, .csv, or .zip</span>
                <input
                type="file"
                accept=".txt, .csv, .zip"
                onChange={handleUpload}
                className="hidden"
                />
            </label>
        </div>
    )
}