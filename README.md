## alban.andrieu.eclipse

[![Travis CI](http://img.shields.io/travis/AlbanAndrieu/ansible-eclipse.svg?style=flat)](http://travis-ci.org/AlbanAndrieu/ansible-eclipse) [![Branch](http://img.shields.io/github/tag/AlbanAndrieu/ansible-eclipse.svg?style=flat-square)](https://github.com/AlbanAndrieu/ansible-eclipse/tree/master) [![Donate](https://img.shields.io/gratipay/AlbanAndrieu.svg?style=flat)](https://www.gratipay.com/AlbanAndrieu)  [![Ansible Galaxy](http://img.shields.io/badge/galaxy-alban.andrieu.eclipse-blue.svg?style=flat)](https://galaxy.ansible.com/list#/roles/1776) [![Platforms](http://img.shields.io/badge/platforms-ubuntu-lightgrey.svg?style=flat)](#)

Ensures that eclipse is properly installed and configured on `Ubuntu` using `Ansible` script.
Default settings is using Eclipse luna.
This ``Simple`` role allows you to install [Eclipse](https://www.eclipse.org) with basic plugins. 

This playbook is be used by [Docker Hub](https://hub.docker.com) to create a [Docker](http://docker.io) image.      

Taken from
------------------

https://www.eclipse.org/downloads/

###Requirements

Tools which might be needed by [Eclipse](https://www.eclipse.org), like jdk, maven...
See available playbook on [GitHub](https://github.com/search?p=3&q=user%3AAlbanAndrieu+ansible%2A&type=Repositories)

### Installation

This role requires at least Ansible `v1.6.3`. 

To install it, run:

    ansible-galaxy install alban.andrieu.eclipse



### Role variables

List of default variables available in the inventory:

```yaml
        eclipse_enabled: yes                       # Enable module
    
    #user: 'albandri' #please override me
    user: "{{ lookup('env','USER') }}"
    eclipse_owner: "{{ user }}"
    eclipse_group: "{{ eclipse_owner }}"
    #home: '~' #please override me
    home: "{{ lookup('env','HOME') }}"
    eclipse_owner_home: "{{ home }}"
    eclipse_base_dir: "/usr/local/eclipse"
    eclipse_link_base_dir: "/opt"
    eclipse_dir_tmp: "/tmp" # or override with "{{ tempdir.stdout }} in order to have be sure to download the file"
    
    ## Most likely you dont need to edit 
    #todo eclipse_service_enabled   : 'yes'
    eclipse_major: "4"
    eclipse_minor: "4"
    #kepler 3.7.2.1
    eclipse_version: "{{eclipse_major}}.{{eclipse_minor}}"
    eclipse_name: "luna"
    eclipse_archive_extracted: "eclipse"
    #eclipse_archive: "eclipse-jee-kepler-SR2-linux-gtk-x86_64.tar.gz"
    #modeling
    #eclipse_archive: "eclipse-modeling-{{eclipse_name}}-R-linux-gtk-x86_64.tar.gz"
    #java
    #eclipse_archive: "eclipse-java-{{eclipse_name}}-SR1-linux-gtk-x86_64.tar.gz"
    #javaee
    eclipse_archive: "eclipse-jee-{{eclipse_name}}-SR1-linux-gtk-x86_64.tar.gz"
    
    #modeling
    #eclipse_url: "https://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/{{eclipse_name}}/R/{{eclipse_archive}}&r=1"
    #java
    #eclipse_url: "https://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/{{eclipse_name}}/SR1/{{eclipse_archive}}&r=1"
    #javaee
    eclipse_url: "https://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/{{eclipse_name}}/SR1/{{eclipse_archive}}&r=1"
    eclipse_home_dir: "{{eclipse_base_dir}}/{{eclipse_name}}-{{eclipse_version}}"
    
    eclipse_plugins_enabled: yes                          # Enable plugins
    eclipse_plugins_emf_enabled: no                       # Enable plugins
    eclipse_plugins_cdt_enabled: no                       # Enable plugins
    eclipse_plugins_cmakeed_enabled: no                   # Enable plugins
    eclipse_plugins_openinterminal_enabled: no            # Enable plugins
    eclipse_plugins_protobuf_enabled: no                  # Enable plugins
    eclipse_plugins_yedit_enabled: no                     # Enable plugins
    eclipse_plugins_shelled_enabled: no                   # Enable plugins
    eclipse_plugins_webpageed_enabled: no                 # Enable plugins
    eclipse_plugins_pydev_enabled: no                     # Enable plugins
    eclipse_plugins_m2e_enabled: no                       # Enable plugins
    eclipse_plugins_subclipse_enabled: no                 # Enable plugins
    
    eclipse_ini_enabled: yes                              # Enable overriding eclipse.ini
    #default is 256m
    eclipse_launcher_XXMaxPermSize: "256m"
    #default is 256m
    eclipse_XXMaxPermSize: "1024m"
    #default is -Xms40m
    eclipse_Xms: "512m"
    #default is -Xmx512m
    eclipse_Xmx: "2048m"
    
    docker_files_generated_directory: "./"
    docker_files_enable: no
    docker_volume_directory                  : "{{ eclipse_base_dir }}"
    docker_working_directory                 : "/home/vagrant"
    docker_image_name                        : "nabla/ansible-eclipse"
```


### Detailed usage guide

Use :

    `docker run -e "DISPLAY=`ipconfig getifaddr en0`:0.0" nabla/ansible-eclipse`

Once [Eclipse](https://www.eclipse.org) is installed using ansible, a [Docker](https://www.docker.com/) [image](https://registry.hub.docker.com/u/nabla/ansible-eclipse/) is automatically created by [Docker Hub](https://registry.hub.docker.com/), 
so please do not hesitate to enhance ansible script it will then improve docker image automatically.

Run the following command :

     `ansible-playbook -i hosts -c local -v eclipse.yml -vvvv --ask-sudo-pass | tee setup.log`


### Authors and license

`alban.andrieu.eclipse` role was written by:
- [Alban Andrieu](fr.linkedin.com/in/nabla/) | [e-mail](mailto:alban.andrieu@free.fr) | [Twitter](https://twitter.com/AlbanAndrieu) | [GitHub](https://github.com/AlbanAndrieu)
- License: [GPLv3](https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29)

### Feedback, bug-reports, requests, ...

Are [welcome](https://github.com/AlbanAndrieu/ansible-eclipse/issues)!

***

README generated by [Ansigenome](https://github.com/nickjj/ansigenome/).
