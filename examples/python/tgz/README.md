tar.gz example service
----------------------
I'm a python service that is bundled into a gzipped tarball using python's setup.py.

running the example
-------------------

Start the VM

```
$ vagrant up
```

Determine which port the VM is listening on for SSH:

```
$ vagrant ssh-config | grep Port
  Port 2202
```

Modify `mendel.yml`'s `dev` port accordingly:

```
$ patch mendel.yml <<EOP
> 7c7
> <     port: 2200
> ---
> >     port: 2202
> EOP
```

Install your development version of `mendel`:

```
# (With a virtual environment activated)
pip install -e /path/to/mendel
```

Deploy to the VM:

```
$ mendel dev deploy
[127.0.0.1] Executing task 'deploy'
[localhost] local: python setup.py sdist

...

Successfully installed new release of myservice service

executing upstart:start
myservice start/running, process 13266

Done.
Disconnecting from 127.0.0.1:2200... done.
```

Test it out!

```
$ curl "http://127.0.0.1:8080/hello"
Hello, Hal 9000!

$ curl "http://127.0.0.1:8080/hello?name=Kevin"
Hello, Kevin!
```
