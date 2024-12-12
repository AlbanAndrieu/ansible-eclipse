# [![Nabla](https://bababou.albandrieu.com/nabla/index/assets/nabla/nabla-4.png)](https://github.com/AlbanAndrieu) roles/alban_andrieu_eclipse

This file was generated by Ansigenome. Do not edit this file directly but instead have a look at the files in the ./meta/ directory.

[![License](http://img.shields.io/:license-apache-blue.svg?style=flat-square)](http://www.apache.org/licenses/LICENSE-2.0.html)
[![Gitter](https://badges.gitter.im/nabla-eclipse/Lobby.svg)](https://gitter.im/nabla-eclipse/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
[![Minimal java version](https://img.shields.io/badge/java-1.8-yellow.svg)](https://img.shields.io/badge/java-1.8-yellow.svg)

[![Branch](http://img.shields.io/github/tag/AlbanAndrieu/ansible-eclipse.svg?style=flat-square)](https://github.com/AlbanAndrieu/ansible-eclipse/tree/master)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-albanandrieu.eclipse-660198.svg?style=flat)](https://galaxy.ansible.com/alban.andrieu/eclipse)
[![Platforms](http://img.shields.io/badge/platforms-el%20/%20macosx%20/%20ubuntu-lightgrey.svg?style=flat)](#)
[![Docker Pulls](https://img.shields.io/docker/pulls/nabla/ansible-eclipse)](https://hub.docker.com/r/nabla/ansible-eclipse)<br/>

Ensures that eclipse is properly installed and configured on `Ubuntu` using `Ansible` script.
Default settings is using Eclipse luna.
This ``Simple`` role allows you to install [Eclipse](https://www.eclipse.org) with basic plugins.

This playbook is be used by [Docker Hub](https://hub.docker.com) to create a [Docker](http://docker.io) image.

See role [ansible-eclipse](https://github.com/AlbanAndrieu/ansible-eclipse) and image [ansible-eclipse](https://hub.docker.com/r/nabla/ansible-eclipse/)

# Table of contents

<!-- toc -->

- [Taken from](#taken-from)
  * [Requirements](#requirements)
  * [Installation](#installation)
  * [Documentation](#documentation)
  * [Role variables](#role-variables)
  * [Detailed usage guide](#detailed-usage-guide)
  * [Contributor](#contributor)
  * [pre-commit](#pre-commit)
  * [npm-groovy-lint groovy formating for Jenkinsfile](#npm-groovy-lint-groovy-formating-for-jenkinsfile)
  * [Linting](#linting)
- [Update README.md](#update-readmemd)
  * [Contributing](#contributing)
  * [Authors and license](#authors-and-license)
- [License](#license)
  * [Feedback, bug-reports, requests, ...](#feedback-bug-reports-requests-)

<!-- tocstop -->

Taken from
------------------

https://www.eclipse.org/downloads/

### Requirements

Tools which might be needed by [Eclipse](https://www.eclipse.org), like jdk, maven...
See available playbook on [GitHub](https://github.com/search?p=3&q=user%3AAlbanAndrieu+ansible%2A&type=Repositories)

### Installation

This role requires at least Ansible `v2.3.1.0`. To install it, run:

Using `ansible-galaxy`:
```shell
$ ansible-galaxy install alban.andrieu.eclipse
```

Using `arm` ([Ansible Role Manager](https://github.com/mirskytech/ansible-role-manager/)):
```shell
$ arm install alban.andrieu.eclipse
```

Using `git`:
```shell
$ git clone https://github.com/AlbanAndrieu/ansible-eclipse.git
```

### Documentation

More information about `alban.andrieu.eclipse` can be found in the
TODO [official alban.andrieu.eclipse documentation](https://docs.debops.org/en/latest/ansible/roles/ansible-eclipse/docs/).


### Role variables

List of default variables available in the inventory:

```YAML
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
#cur_dir: "{{lookup('pipe','pwd')}}"
## Most likely you dont need to edit
#todo eclipse_service_enabled   : 'yes'

#eclipse_name: "kepler" 3.7.2.1
#eclipse_name: "luna" 4.4
#eclipse_name: "mars" 4.5
#eclipse_name: "neon" 4.6
eclipse_name: "neon"
eclipse_major: "4"
eclipse_minor: "6"
eclipse_version: "{{eclipse_major}}.{{eclipse_minor}}"

eclipse_archive_extracted: "eclipse"
#modeling
#eclipse_archive: "eclipse-modeling-{{eclipse_name}}-R-linux-gtk-x86_64.tar.gz"
#java
#eclipse_archive: "eclipse-java-{{eclipse_name}}-SR1-linux-gtk-x86_64.tar.gz"
#javaee
#eclipse_archive: "eclipse-jee-{{eclipse_name}}-SR1-linux-gtk-x86_64.tar.gz"
#eclipse_archive: "eclipse-jee-{{eclipse_name}}-R-linux-gtk-x86_64.tar.gz"
eclipse_archive: "eclipse-jee-{{eclipse_name}}-3-RC3-linux-gtk-x86_64.tar.gz"

#eclipse_url: "https://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/{{eclipse_name}}/R/{{eclipse_archive}}&r=1"
#eclipse_url: "http://eclipse.mirror.triple-it.nl/technology/epp/downloads/release/{{eclipse_name}}/R/{{eclipse_archive}}"
eclipse_url: "http://eclipse.mirror.triple-it.nl/technology/epp/downloads/release/{{eclipse_name}}/3.RC3/{{eclipse_archive}}"

eclipse_home_dir: "{{ eclipse_base_dir }}/{{ eclipse_name }}-{{ eclipse_version }}"
#eclipse_desktop: "/usr/share/applications/eclipse.desktop"
eclipse_desktop: "{{ eclipse_owner_home }}/.local/share/applications/eclipse.desktop"

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
#eclipse_launcher_XXMaxPermSize: "512m"
eclipse_launcher_XXMaxPermSize: ""
#default is 256m
#eclipse_XXMaxPermSize: "1024m"
eclipse_XXMaxPermSize: ""
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

List of internal variables used by the role:

    eclipse_folder
    eclipse_home
    eclipse
### Detailed usage guide

Use :

    `docker run -e "DISPLAY=`ipconfig getifaddr en0`:0.0" nabla/ansible-eclipse`
    `docker run  -it --entrypoint /bin/bash nabla/ansible-eclipse`

Once [Eclipse](https://www.eclipse.org) is installed using ansible, a [Docker](https://www.docker.com/) [image](https://registry.hub.docker.com/u/nabla/ansible-eclipse/) is automatically created by [Docker Hub](https://registry.hub.docker.com/),
so please do not hesitate to enhance ansible script it will then improve docker image automatically.

Run the following command :

```bash
ansible -m setup localhost
cd roles
ln -s ../ albanandrieu.eclipse
cd ..
ansible-playbook -i hosts -c local eclipse.yml -vvv --ask-become-pass --become | tee setup.log
ANSIBLE_NOCOLOR=True && ansible-playbook -i hosts -c local -v eclipse.yml -vvv --ask-become-pass --become > eclipse.log  2>&1
```

### Contributor

- Yngve Inntjore Levinsen
- Alban Andrieu, alban.andrieu@free.com### Testing
```shell
$ ansible-galaxy install alban.andrieu.eclipse
$ vagrant up
```


### pre-commit

See [pre-commit](http://pre-commit.com/)
Run `pre-commit install`

First time run `cp hooks/hooks/* .git/hooks/`
or `git clone git@github.com:AlbanAndrieu/nabla-hooks.git hooks && rm -Rf ./.git/hooks && ln -s ../hooks/hooks ./.git/hooks`

Run `pre-commit run --all-files`

Run `SKIP=ansible-lint git commit -am 'Add key'`
Run `git commit -am 'Add key' --no-verify`

### npm-groovy-lint groovy formating for Jenkinsfile

Tested with nodejs 12 and 16 on ubuntu 20 and 21 (not working with nodejs 11 and 16)

```bash
npm install -g npm-groovy-lint@8.2.0
npm-groovy-lint --format
ls -lrta .groovylintrc.json
```

### Linting

```shell
$ git add tasks/features.yml # First add your file, then
$ pre-commit run ansible-lint
```



## Update README.md


  * [github-markdown-toc](https://github.com/jonschlinkert/markdown-toc)
  * With [github-markdown-toc](https://github.com/Lucas-C/pre-commit-hooks-nodejs)

```bash
npm install --save markdown-toc
markdown-toc README.md
markdown-toc CHANGELOG.md  -i
```

```
git add README.md
pre-commit run markdown-toc
```

### Contributing

The [issue tracker](https://github.com/AlbanAndrieu/ansible-eclipse/issues) is the preferred channel for bug reports, features requests and submitting pull requests.

For pull requests, editor preferences are available in the [editor config](.editorconfig) for easy use in common text editors. Read more and download plugins at <http://editorconfig.org>.

In lieu of a formal styleguide, take care to maintain the existing coding style. Add unit tests and examples for any new or changed functionality.

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

### Authors and license

`roles/alban_andrieu_eclipse` role was written by:

- Yngve Inntjore Levinsen | [GitHub](https://github.com/ Eothred)
- [Alban Andrieu](fr.linkedin.com/in/nabla/) | [e-mail](mailto:alban.andrieu@free.com) | [Twitter](https://twitter.com/AlbanAndrieu) | [GitHub](https://github.com/AlbanAndrieu)

License
-------

- License: [GPLv3](https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29)

### Feedback, bug-reports, requests, ...

Are [welcome](https://github.com/AlbanAndrieu/ansible-eclipse/issues)!

***

This role is part of the [Nabla](https://github.com/AlbanAndrieu) project.
README generated by [Ansigenome](https://github.com/nickjj/ansigenome/).

***

Alban Andrieu

[linkedin](fr.linkedin.com/in/nabla/)
