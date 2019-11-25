#!bin/env python3
import os

base_dir = os.getenv('BASE_DIR')
ps_version = os.getenv('PS_VERSION')
ps_revision = os.getenv('PS_REVISION')

ps_version_upstream, ps_version_percona = ps_version.split('-')
ps_version_major = ps_version_upstream.split('.')[0] + '.' + ps_version_upstream.split('.')[1]

# 8.0
ps80_binaries = (
  'bin/mysql', 'bin/mysqld', 'bin/ps-admin', 'bin/mysqladmin', 'bin/mysqlbinlog',
  'bin/mysqldump', 'bin/mysqldumpslow', 'bin/mysqlimport', 'bin/mysqlpump', 'bin/mysqlshow',
  'bin/mysqlslap', 'bin/mysqlcheck', 'bin/mysql_config_editor', 'bin/mysql_config', 'bin/mysql_ldb',
  'bin/mysqlrouter', 'bin/mysqlrouter_passwd', 'bin/mysqlrouter_plugin_info', 'bin/mysql_secure_installation', 'bin/mysql_ssl_rsa_setup',
  'bin/mysql_upgrade', 'bin/mysql_tzinfo_to_sql'
)
ps80_plugins = (
  ('audit_log','audit_log.so'),('mysql_no_login','mysql_no_login.so'),('validate_password','validate_password.so'),
  ('version_tokens','version_token.so'),('rpl_semi_sync_master','semisync_master.so'),('rpl_semi_sync_slave','semisync_slave.so'),
  ('group_replication','group_replication.so'),('clone','mysql_clone.so'),('data_masking','data_masking.so')
)
ps80_functions = (
  ('fnv1a_64', 'libfnv1a_udf.so', 'INTEGER'),('fnv_64', 'libfnv_udf.so', 'INTEGER'),('murmur_hash', 'libmurmur_udf.so', 'INTEGER'),
  ('version_tokens_set', 'version_token.so', 'STRING'),('version_tokens_show', 'version_token.so', 'STRING'),('version_tokens_edit', 'version_token.so', 'STRING'),
  ('version_tokens_delete', 'version_token.so', 'STRING'),('version_tokens_lock_shared', 'version_token.so', 'INT'),('version_tokens_lock_exclusive', 'version_token.so', 'INT'),
  ('version_tokens_unlock', 'version_token.so', 'INT'),('service_get_read_locks', 'locking_service.so', 'INT'),('service_get_write_locks', 'locking_service.so', 'INT'),
  ('service_release_locks', 'locking_service.so', 'INT')
)
ps80_files = (
  'lib/libHotBackup.so', 'lib/libmysqlharness.a', 'lib/libmysqlharness.so.1',
  'lib/libmysqlrouter_http.so.1', 'lib/libmysqlrouter.so.1', 'lib/libmysqlservices.a',
  'lib/libperconaserverclient.a', 'lib/libperconaserverclient.so.21.1.17' ,'lib/mysql/libjemalloc.so.1',
  'lib/mysql/plugin/ha_tokudb.so', 'lib/mysql/plugin/ha_rocksdb.so', 'lib/mysql/plugin/audit_log.so',
  'lib/mysql/plugin/auth_pam.so', 'lib/mysql/plugin/auth_pam_compat.so', 'lib/mysql/plugin/data_masking.so',
  'lib/mysql/plugin/data_masking.ini', 'lib/mysql/plugin/tokudb_backup.so','lib/mysql/plugin/keyring_file.so',
  'lib/mysql/plugin/keyring_udf.so', 'lib/mysql/plugin/keyring_vault.so'
)
ps80_symlinks = (
  ('lib/libmysqlharness.so','lib/libmysqlharness.so.1'),('lib/libmysqlrouter_http.so','lib/libmysqlrouter_http.so.1'),
  ('lib/libmysqlrouter.so','lib/libmysqlrouter.so.1'),('lib/libperconaserverclient.so.21','lib/libperconaserverclient.so.21.1.17'),
  ('lib/libperconaserverclient.so','lib/libperconaserverclient.so.21.1.17'),('lib/mysql/libjemalloc.so','lib/mysql/libjemalloc.so.1')
)

# 5.7
ps57_binaries = (
  'bin/mysql', 'bin/mysqld', 'bin/ps-admin', 'bin/mysqladmin', 'bin/mysqlbinlog',
  'bin/mysqldump', 'bin/mysqldumpslow', 'bin/mysqlimport', 'bin/mysqlpump', 'bin/mysqlshow',
  'bin/mysqlslap', 'bin/mysqlcheck', 'bin/mysql_config_editor', 'bin/mysql_config', 'bin/mysql_ldb',
  'bin/mysql_secure_installation', 'bin/mysql_ssl_rsa_setup', 'bin/mysql_upgrade', 'bin/mysql_tzinfo_to_sql'
)
ps57_plugins = (
  ('audit_log','audit_log.so'),('mysql_no_login','mysql_no_login.so'),('validate_password','validate_password.so'),
  ('version_tokens','version_token.so'),('rpl_semi_sync_master','semisync_master.so'),('rpl_semi_sync_slave','semisync_slave.so'),
  ('group_replication','group_replication.so')
)
ps57_functions = (
  ('fnv1a_64', 'libfnv1a_udf.so', 'INTEGER'),('fnv_64', 'libfnv_udf.so', 'INTEGER'),('murmur_hash', 'libmurmur_udf.so', 'INTEGER'),
  ('version_tokens_set', 'version_token.so', 'STRING'),('version_tokens_show', 'version_token.so', 'STRING'),('version_tokens_edit', 'version_token.so', 'STRING'),
  ('version_tokens_delete', 'version_token.so', 'STRING'),('version_tokens_lock_shared', 'version_token.so', 'INT'),('version_tokens_lock_exclusive', 'version_token.so', 'INT'),
  ('version_tokens_unlock', 'version_token.so', 'INT'),('service_get_read_locks', 'locking_service.so', 'INT'),('service_get_write_locks', 'locking_service.so', 'INT'),
  ('service_release_locks', 'locking_service.so', 'INT')
)
ps57_files = (
  'lib/libHotBackup.so', 'lib/libmysqlharness.a', 'lib/libmysqlharness.so.1',
  'lib/libmysqlrouter_http.so.1', 'lib/libmysqlrouter.so.1', 'lib/libmysqlservices.a',
  'lib/libperconaserverclient.a', 'lib/libperconaserverclient.so.21.1.17' ,'lib/mysql/libjemalloc.so.1',
  'lib/mysql/plugin/ha_tokudb.so', 'lib/mysql/plugin/ha_rocksdb.so', 'lib/mysql/plugin/audit_log.so',
  'lib/mysql/plugin/auth_pam.so', 'lib/mysql/plugin/auth_pam_compat.so', 'lib/mysql/plugin/data_masking.so',
  'lib/mysql/plugin/data_masking.ini', 'lib/mysql/plugin/tokudb_backup.so','lib/mysql/plugin/keyring_file.so',
  'lib/mysql/plugin/keyring_udf.so', 'lib/mysql/plugin/keyring_vault.so'
)
ps57_symlinks = (
  ('lib/libmysqlharness.so','lib/libmysqlharness.so.1'),('lib/libmysqlrouter_http.so','lib/libmysqlrouter_http.so.1'),
  ('lib/libmysqlrouter.so','lib/libmysqlrouter.so.1'),('lib/libperconaserverclient.so.21','lib/libperconaserverclient.so.21.1.17'),
  ('lib/libperconaserverclient.so','lib/libperconaserverclient.so.21.1.17')
)

# 5.6
ps56_binaries = (
  'bin/mysql', 'sbin/mysqld', 'bin/mysqladmin', 'bin/mysqlbinlog', 'bin/mysqldump',
  'bin/mysqldumpslow', 'bin/mysqlimport', 'bin/mysqlshow', 'bin/mysqlslap', 'bin/mysqlcheck',
  'bin/mysql_config_editor', 'bin/mysql_secure_installation', 'bin/mysql_upgrade', 'bin/mysql_tzinfo_to_sql')
ps56_plugins = (
  ('audit_log','audit_log.so'),('mysql_no_login','mysql_no_login.so'),('validate_password','validate_password.so'),
  ('rpl_semi_sync_master','semisync_master.so'),('rpl_semi_sync_slave','semisync_slave.so')
)
ps56_functions = (
  ('fnv1a_64', 'libfnv1a_udf.so', 'INTEGER'),('fnv_64', 'libfnv_udf.so', 'INTEGER'),('murmur_hash', 'libmurmur_udf.so', 'INTEGER')
)
ps56_files = (
  'lib/libHotBackup.so', 'lib/libmysqlharness.a', 'lib/libmysqlharness.so.1',
  'lib/libmysqlrouter_http.so.1', 'lib/libmysqlrouter.so.1', 'lib/libmysqlservices.a',
  'lib/libperconaserverclient.a', 'lib/libperconaserverclient.so.21.1.17' ,'lib/mysql/libjemalloc.so.1',
  'lib/mysql/plugin/ha_tokudb.so', 'lib/mysql/plugin/ha_rocksdb.so', 'lib/mysql/plugin/audit_log.so',
  'lib/mysql/plugin/auth_pam.so', 'lib/mysql/plugin/auth_pam_compat.so', 'lib/mysql/plugin/data_masking.so',
  'lib/mysql/plugin/data_masking.ini', 'lib/mysql/plugin/tokudb_backup.so','lib/mysql/plugin/keyring_file.so',
  'lib/mysql/plugin/keyring_udf.so', 'lib/mysql/plugin/keyring_vault.so'
)
ps56_symlinks = (
  ('lib/libmysqlharness.so','lib/libmysqlharness.so.1'),('lib/libmysqlrouter_http.so','lib/libmysqlrouter_http.so.1'),
  ('lib/libmysqlrouter.so','lib/libmysqlrouter.so.1'),('lib/libperconaserverclient.so.21','lib/libperconaserverclient.so.21.1.17'),
  ('lib/libperconaserverclient.so','lib/libperconaserverclient.so.21.1.17')
)
#####

if ps_version_major == '8.0':
    ps_binaries = ps80_binaries
    ps_plugins = ps80_plugins
    ps_functions = ps80_functions
    ps_files = ps80_files
    ps_symlinks = ps80_symlinks
elif ps_version_major == '5.7':
    ps_binaries = ps57_binaries
    ps_plugins = ps57_plugins
    ps_functions = ps57_functions
    ps_files = ps57_files
    ps_symlinks = ps57_symlinks
elif ps_version_major == '5.6':
    ps_binaries = ps56_binaries
    ps_plugins = ps56_plugins
    ps_functions = ps56_functions
    ps_files = ps56_files
    ps_symlinks = ps56_symlinks