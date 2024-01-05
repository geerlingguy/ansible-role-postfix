# Ansible Role: Postfix

[![CI](https://github.com/geerlingguy/ansible-role-postfix/workflows/CI/badge.svg?event=push)](https://github.com/geerlingguy/ansible-role-postfix/actions?query=workflow%3ACI)

Installs postfix on RedHat/CentOS or Debian/Ubuntu.

## Requirements

If you're using this as an SMTP relay server, you will need to open TCP port 25 in your server firewall.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    postfix_config_file: /etc/postfix/main.cf

The path to the Postfix `main.cf` configuration file.

    postfix_service_state: started
    postfix_service_enabled: true

The state in which the Postfix service should be after this role runs, and whether to enable the service on startup.

    postfix_inet_interfaces: localhost
    postfix_inet_protocols: all

Options for values `inet_interfaces` and `inet_protocols` in the `main.cf` file. 

    postfix_smtpd_banner
    postfix_mynetworks
    postfix_smtpd_tls_cert_file
    postfix_smtpd_tls_key_file
    postfix_smtpd_tls_security_level
    postfix_maillog_file
    postfix_myhostname
    postfix_smtpd_relay_restrictions
    postfix_mydestination

Options that will be set if the built-in template is used.

    postfix_templates

List of `src` and `dest` with templates to deploy.

    postfix_transport_template
    postfix_transport_file

Options for the postfix tranport file and template. This is handeled outside of other templates because it has to be managed in a different way.

    postfix_transports

List of entries for the postfix transports file.

## Dependencies

None.

## Example Playbook

    - hosts: all
      roles:
        - geerlingguy.postfix
      vars:
        postfix_templates:
          - src: main.cf.j2
            dest: /etc/postfix/main.cf
          - src: master.cf.j2
            dest: /etc/postfix/master.cf
            mode: 0664
            owner: root
            group: postfix
        postfix_transports:
          - pattern: *@subdomain.example.com
            method: smtp
            nexthop: 10.0.0.2
        postfix_dkim_socket: "unix:/opendkim/opendkim.sock"

## License

MIT / BSD

## Author Information

This role was created in 2014 by [Jeff Geerling](https://www.jeffgeerling.com/), author of [Ansible for DevOps](https://www.ansiblefordevops.com/).
