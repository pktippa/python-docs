# Anaconda

## Setting Up PATH environment Variable.

### For Windows

If anaconda is Installed in `D:\softs\anaconda3`


```batch
> set PATH=%PATH%;D:\softs\anaconda3;D:\softs\anaconda3\Scripts;
```


## Running anaconda behind proxy

Have the `.condarc` file in USER Home directory.

with below content, with the changed proxy settings and save it.

```txt
channels:
  - conda-forge
  - defaults

# Show channel URLs when displaying what is going to be downloaded and
# in 'conda list'. The default is False.
show_channel_urls: true
allow_other_channels: true

proxy_servers:
  http: http://proxy_username:proxy_password@proxy_host:proxy_port
  https: http://proxy_username:proxy_password@proxy_host:proxy_port


ssl_verify: false

```

## Setting up new Environment

### Listing all environments

```sh
$ conda env list
```

### Creating the environment

```sh
$ conda create -n newenv python=3.6 anaconda
```

### Activating the newly created environment

```sh
$ source activate newenv
```

### Look at the packages Installed on an Environment

```sh
$ conda list
```

### Installing packages from file

```sh
$ conda install -y --file <file_name>
```

### Deactivating the environment

#### For Current Environment

```sh
$ source deactivate
```

#### For Other Environment

```sh
$ source deactivate newenv
```

### Removing the environment that is no longer in use.

```sh
$ conda remove -n yourenvname --all
```