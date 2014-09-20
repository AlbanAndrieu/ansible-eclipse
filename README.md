# ansible-eclipse

A role for installing eclipse.


## Actions

- Ensures that eclipse is installed (using `apt`)


## Usage:
```
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

```

## License

MIT
