import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_postfix_package(host):
    pkg = host.package('postfix')

    assert pkg.is_installed


def test_postfix_service(host):
    service = host.service('postfix')

    assert service.is_running
    assert service.is_enabled


def test_postfix_config_file(host):
    f = host.file('/etc/postfix/main.cf')

    assert f.is_file
    assert f.contains(r'^inet_interfaces = localhost$')
