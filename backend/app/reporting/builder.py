from app.schemas import Domain, Finding, Report, Vendor


def build_report(vendor: Vendor, findings: list[Finding], panel_version: str) -> Report:
    grouped: dict[Domain, list[Finding]] = {d: [] for d in Domain}
    for f in sorted(findings, key=lambda f: f.variant_id):
        grouped[f.domain].append(f)
    return Report(vendor=vendor, findings_by_domain=grouped, panel_version=panel_version)
