
__config__ = {
    "wls_coherence_configs.domain_folder": dict(
        description = "Domain folder, usually /maerskwas/domains/domainName",
        default = None,
    ),
    "wls_coherence_configs.oracle_db_url" : dict(
        description = 'Oracle database URL',
        default = None,
    ),
    "wls_coherence_configs.ds_refdata_user" : dict(
        description = 'user name for REFDATA db',
        default = None,
    ),
    "wls_coherence_configs.ds_refdata_password" : dict(
        description = 'password for REFDATA db',
        default = None,
    ),
    "wls_coherence_configs.ds_refdata_schema" : dict(
        description = 'Schema for REFDATA db',
        default = None,
    ),
    "wls_coherence_configs.ds_xleap_user" : dict(
        description = 'user name for XLEAP db',
        default = None,
    ),
    "wls_coherence_configs.ds_xleap_password" : dict(
        description = 'password for XLEAP db',
        default = None,
    ),
    "wls_coherence_configs.ds_xleap_password" : dict(
        description = 'password for XLEAP db',
        default = None,
    ),
    "wls_coherence_configs.log_level" : dict(
        description = 'Coherence log level',
        default = None,
    ),
    "wls_coherence_configs.log_dir" : dict(
        description = 'full path where logs will be collected',
        default = None,
    ),
    "wls_coherence_configs.tangosol_coherence_member" : dict(
        description = 'Tangosol coherence member',
        default = None,
    )
}
