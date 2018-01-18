# Anaconda

## Setting Up PATH environment Variable.

### For Windows

If anaconda is Installed in `D:\softs\anaconda3`


```batch
> set PATH=%PATH%;D:\softs\anaconda3;D:\softs\anaconda3\Scripts;
```


## Running anaconda behind proxy

Have the `.condarc` file in USER Home directory.

TODO

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