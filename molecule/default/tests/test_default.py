import os

import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('pkg', [
  'unzip',
  'java-1.8.0-openjdk-devel',
  'python2-pip'
])
def test_pkg(host, pkg):
    package = host.package(pkg)

    assert package.is_installed
