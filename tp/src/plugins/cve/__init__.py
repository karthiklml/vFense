CveCollection = 'cve'
WindowsSecurityBulletinCollection = 'windows_security_bulletin'
UbuntuSecurityBulletinCollection = 'ubuntu_security_bulletin'
DebianSecurityBulletinCollection = 'debian_security_bulletin'
RedHatSecurityBulletinCollection = 'redhat_security_bulletin'

class CveKey():
    CveId = 'cve_id'
    CveName = 'cve_name'
    CveCategories = 'vulnerability_categories'
    CveDescriptions = 'cve_descriptions'
    CveRefs = 'cve_refs'
    CveReject = 'cve_reject'
    CveSev = 'cve_sev'
    CvePublishedDate = 'cve_published_date'
    CveModifiedDate = 'cve_modified_date'
    CveVulnsSoft = 'cve_vulns_soft'
    CvssScore = 'cvss_score'
    CvssBaseScore = 'cvss_base_score'
    CvssImpactSubScore = 'cvss_impact_subscore'
    CvssExploitSubScore = 'cvss_exploit_subscore'
    CvssVector = 'cvss_vector'
    CvssVersion = 'cvss_version'
    Type = 'type'

class CveIndexes():
    CveCategories = 'vulnerability_categories'

class WindowsSecurityBulletinKey():
    Id = 'id'
    DatePosted = 'date_posted'
    BulletinId = 'bulletin_id'
    BulletinKb = 'bulletin_kb'
    BulletinSeverity = 'bulletin_severity'
    BulletinImpact = 'bulletin_impact'
    Title = 'bulletin_title'
    AffectedProduct = 'affected_product'
    ComponentKb = 'component_kb'
    AffectedComponent = 'affected_component'
    ComponentImpact = 'component_impact'
    ComponentSeverity = 'component_severity'
    SupersedesBulletinId = 'supercedes_bulletin_id'
    SupersedesBulletinKb = 'supercedes_bulletin_kb'
    Supersedes = 'supercedes'
    Reboot = 'reboot'
    CveIds = 'cve_ids'

class WindowsSecurityBulletinIndexes():
    BulletinId = 'bulletin_id'
    ComponentKb = 'component_kb'
    CveIds = 'cve_ids'

class UbuntuSecurityBulletinKey():
    Id = 'id'
    DatePosted = 'date_posted'
    BulletinId = 'bulletin_id'
    Summary = 'bulletin_summary'
    Details = 'bulletin_details'
    Apps = 'apps'
    Os_string = 'os_string'
    CveIds = 'cve_ids'

class UbuntuSecurityBulletinIndexes():
    BulletinId = 'bulletin_id'
    NameAndVersion = 'name_and_version'
    CveIds = 'cve_ids'
