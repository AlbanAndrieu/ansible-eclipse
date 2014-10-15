ansible-eclipse
====================

A role for installing eclipse.

[![Build Status](https://api.travis-ci.org/AlbanAndrieu/ansible-eclipse.png?branch=master)](https://travis-ci.org/AlbanAndrieu/ansible-eclipse)

## Actions

- Ensures that eclipse is installed (using `ansible`)
- Once eclipse is installed using ansible, a docker image is automatically created, so please do not hesitate to enhance ansible script it will then improve docker image.

Usage example
------------

    - name: Install eclipse
      connection: local  
      hosts: workstation
      remote_user: albandri
      
      roles:
        - role: eclipse     
      
      vars:    
          eclipse_base_dir: /workspace/eclipse     
          eclipse_owner: albandri
          eclipse_group: albandri
        
Requirements
------------

none

Dependencies
------------

none

License
-------

MIT

#### Feedback, bug-reports, requests, ...

Are [welcome](https://github.com/AlbanAndrieu/ansible-eclipse/issues)!
