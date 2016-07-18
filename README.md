![alt tag](https://camo.githubusercontent.com/280a5866b9f4bfb939799776e9b651e986c6600c/68747470733a2f2f77696b692e67616c61787970726f6a6563742e6f72672f496d616765732f47616c6178794c6f676f3f616374696f6e3d41747461636846696c6526646f3d676574267461726765743d67616c6178795f70726f6a6563745f6c6f676f2e6a7067)

# Galaxy-Godocker

A REST based runner for executing Galaxy jobs using GoDocker.

GoDocker is a batch computing/cluster management tool using Docker as execution/isolation system.
Galaxy is designed to run jobs on your local system by default, but it can be configured to run jobs on a cluster. The front-end Galaxy application runs on a single server as usual, but tools are run on cluster nodes instead. Here, we use GoDocker system to manage authentication, scheduling and execution of jobs.

REST API of GoDocker is defined [here](http://www.genouest.org/api/godocker-api/#/)

# Galaxy Quickstart

Galaxy requires Python 2.7 To check your python version, run:

```
    $ python -V
    Python 2.7.3
```

Runner should be configured for the requirements and user information of GoDocker and is available at ``job_conf.xml``.
A template of job_conf.xml is available [here](https://github.com/varunshankar/galaxy-godocker/blob/master/bin/job_conf.xml/)

Start Galaxy:

```
    $ sh run.sh
```
Once Galaxy completes startup, you should be able to view Galaxy in your
browser at:

http://localhost:8080

  
You may wish to make changes from the default configuration. This can be
done in the ``config/galaxy.ini`` file. Tools can be either installed
from the Tool Shed or added manually. For details please see the Galaxy
wiki:

https://wiki.galaxyproject.org/Admin/Tools/AddToolFromToolShedTutorial

Not all dependencies are included for the tools provided in the sample
``tool_conf.xml``. A full list of external dependencies is available at:

https://wiki.galaxyproject.org/Admin/Tools/ToolDependencies

The latest information about Galaxy is available via https://galaxyproject.org/

# Documentation

Runner documentation is available [here](https://github.com/varunshankar/galaxy-godocker/wiki/%5BDOCUMENTATION%5D-GoDocker-runner-for-galaxy)

Interested in creating a runner? Tutorial is available [here](https://github.com/varunshankar/galaxy-godocker/wiki/%5BTUTORIAL%5D-Create-a-new-runner-for-Galaxy)

# Architecture

![alt-image](https://github.com/varunshankar/galaxy-godocker/blob/master/Go-Docker.PNG)






