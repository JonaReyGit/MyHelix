'use client'

import { useState } from 'react'
import { createClient } from '@/lib/supabase/client'

export default function LoginPage() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [status, setStatus] = useState('')

  async function submit(mode: 'signin' | 'signup') {
    const supabase = createClient()
    setStatus('Working...')

    const { error } =
      mode === 'signin'
        ? await supabase.auth.signInWithPassword({ email, password })
        : await supabase.auth.signUp({ email, password })

    setStatus(error ? error.message : 'Signed in - go to /upload')
  }

  return (
    <div className="min-h-screen flex items-center justify-center p-6">
      <div className="w-full max-w-sm flex flex-col gap-3">
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="border rounded px-3 py-2"
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="border rounded px-3 py-2"
        />
        <div className="flex gap-2">
          <button onClick={() => submit('signin')} className="flex-1 border rounded px-3 py-2">
            Sign in
          </button>
          <button onClick={() => submit('signup')} className="flex-1 border rounded px-3 py-2">
            Sign up
          </button>
        </div>
        {status && <p className="text-sm text-gray-600">{status}</p>}
      </div>
    </div>
  )
}
