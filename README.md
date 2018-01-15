# BitBrew Events Analysis

Descriptive analytics using **python 3.6** for BitBrew event data.
See BitBrew's [official documentation](https://github.com/BitBrew/event-docs) for more details. 

## Usage

Follow these instructions for first-use.

1. Create the configuration file: `cp settings/.env.example settings/.env`
1. Add your vhost, user and password in the configuration file: `nano settings/.env` or `vim settings/.env`
1. Install BitBrew's [node consumer](https://github.com/BitBrew/queue-consumer) for RabbitMQ.
1. Add file permission to the consumer bash-script for this repo: `chmod u+rx consumer.sh`
1. Create a virtual environment and install the requirements:
    * `virtualenv --python=python3 venv`
    * `source venv/bin/activate`
    * `pip install -r requirements.txt`
1. Run the setup script: `python setup.py`. Note: the setup script downloads the last 48h from the consumer. This might take a while.

After the first-use installation, you can run the repo as following:

```bash
python main.py --filename {filename} --pdf --update
```

Options:
``` 
    -f,  --filename    The filename output. Default: 'analysis'.               
    -p,  --pdf         Possible file extension.
    -u,  --update      Updates the log_queue.txt file by running the consumer.sh bash-script.
                       Warning: This might take a while.
```



## Contributions and authors

Contact the main developer. 

* **Main developer:** Rodrigo Hernandez Mota (rohdzmota@gmail.com)


## License

See **LICENSE.md** file for more information.