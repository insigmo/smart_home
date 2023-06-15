import logging

import ioc


class ServicesRegistrator:
    @classmethod
    def register_services(cls, environment_settings: CephManagementEnvironmentSettings):
        etcd_host, etcd_port = environment_settings.etcd_endpoints[0]

        client = etcd3.Etcd3Client(etcd_host, etcd_port)
        etcd_storage_client = EtcdStorageClient(client)

        settings_key = environment_settings.etcd_config_key
        ceph_management_api_settings_json = etcd_storage_client.get(settings_key)
        ceph_management_settings = CephManagementApiSettings(**ceph_management_api_settings_json)
        LoggingConfigurator.configure(ceph_management_settings.log_level)
        cls._logger().info(f"ceph_management_settings {ceph_management_settings}")
        ioc.register(
            StorageServiceAbstract,
            lambda c, ds=ceph_management_settings: cls._get_ceph_management_service(ds)
        )
        cls._logger().info("Services are registered")

    @classmethod
    def _get_ceph_management_service(cls, ceph_settings: CephManagementApiSettings) -> StorageServiceAbstract:
        return StorageService(ceph_settings)

    @classmethod
    def _logger(cls) -> logging.Logger:
        return logging.getLogger(__name__)
