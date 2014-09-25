ansible-eclipse
====================

A role for installing eclipse.

[![Build Status](https://api.travis-ci.org/AlbanAndrieu/ansible-eclipse.png?branch=master)](https://travis-ci.org/AlbanAndrieu/ansible-eclipse)

## Actions

- Ensures that eclipse is installed (using `apt`)


Usage example
------------

  - name: Install eclipse
    connection: local  
    hosts: workstation
    remote_user: albandri
  #  connection: local
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
