# Ansible JBoss Common Role [![Build Status](https://api.travis-ci.org/redhat-cop/ansible-role-jboss-common.svg)](https://travis-ci.org/redhat-cop/ansible-role-jboss-common)

A role to handle the common setup required for the other roles in the JBoss family:

- [JBoss EAP](https://github.com/rhtconsulting/jboss_eap)
- [JBoss BxMS](https://github.com/rhtconsulting/jboss_bxms)
- [JBoss Fuse](https://github.com/rhtconsulting/jboss_fuse)
- [JBoss AMQ](https://github.com/rhtconsulting/jboss_amq)
- [JBoss Datagrid](https://github.com/redhat-cop/jboss_datagrid)

The main task done are:

- Set up CentOS or RHEL repositories (e.g: EPEL)
- Register host in RHN for RHEL hosts
- Install OS packages
- Install PIP and Python dependencies
- Install JDK packages aligned with OS. In case of latest OS versions, JDK 11 will be installed.

## Role Variables

Main role variables:

- **install_java**: Install JDK packages. Default value `true`
- **jboss_java_pkg_name**: Install JDK 8 package. Default value `java-1.8.0-openjdk-devel`
- **jboss_java_11_pkg_name**: Install JDK 11 package. Default value `java-11-openjdk-devel`
- **transfer_method**: How to copy the binaries into inventory hosts. Default value `csp-to-host`
- **rhsm_subscribe_host**: Subscribe host in RHN. Default value `true`
- **rhsm_disable_existing_repositories**: Disable existing repositories. Default value `true`
- **rhsm_enable_required_repositories**: Enable required repositories. Default value `true`
- **rhsm_repositories**: List of default repositories to enable,
- **install_pip_dependencies**: Install PIP dependencies. Default value `true`
- **packages_to_install**: . Empty list as default value

## Example Playbooks

## TODO

## License

[LICENSE](./LICENSE)
