# My Profile

This is a README.md file for the **My Profile Project**.

## Overview

This project serves as my personal profile website, showcasing my skills, background, and achievements.

## Design Reference

The design of the profile page is referenced from [seanoshea.me](https://seanoshea.me/).

## Deployment

To deploy this project, follow the steps outlined in the DigitalOcean tutorial:
- [Initial Server Setup](https://www.digitalocean.com/community/tutorial-collections/initial-server-setup)

- Clone the project repository into the `/home/djangoadmin/` directory:

    ```bash
    git clone https://github.com/koyonkym/myprofile.git /home/djangoadmin/
    ```

- [How To Set Up Django with Postgres, Nginx, and Gunicorn on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu)

After following the instructions in the tutorial, make sure to run the following command to ensure correct permissions:

```bash
sudo chmod o+x /home/djangoadmin/
```

This command grants execute permissions to other users on the `/home/djangoadmin/` directory.

- Create a `local_settings.py` file in the same directory as your `settings.py` file. Set the following variables:

    ```python
    # myprofile/myprofile/local_settings.py

    SECRET_KEY = 'your_secret_key'
    DEBUG = False
    ALLOWED_HOSTS = ['your_domain.com', 'your_IP_address']

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'your_database_name',
            'USER': 'your_database_user',
            'PASSWORD': 'your_database_password',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
    ```

- In your `settings.py` file, set the `STATIC_ROOT` variable to define where Django should collect static files:

    ```python
    # myprofile/myprofile/settings.py

    STATIC_ROOT = BASE_DIR / 'static'
    ```

After completing these steps, you should be able to successfully deploy your Django project.

### Configuration Note

Depending on your project structure, you may need to configure the Nginx `location` block for serving static files differently. If your static files are located in a subdirectory within the project directory, you should use the `alias` directive instead of the `root` directive.

Example:

```nginx
location /static/ {
    alias /home/sammy/myprofile/static/;
}
```

This ensures that Nginx correctly serves static files from the specified directory.

## Deployment (Second Time)

After making changes to the project, you can update the deployed version by following these steps:

1. Pull the latest changes from the GitHub repository:

    ```bash
    git pull origin main
    ```

    If you encounter the error message `error: Your local changes to the following files would be overwritten by merge:`, and those files don't need to be kept (such as files in the `__pycache__` directory), you can discard the local changes by running:

    ```bash
    git checkout -- <file_path>
    ```

    Then, proceed to pull the changes again.

2. Activate the virtual environment:

    ```bash
    source .venv/bin/activate
    ```

3. Install packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply any database migrations:

    ```bash
    python manage.py migrate
    ```

    This step is necessary if there are any updates in the models.

5. Collect static files:

    ```bash
    python manage.py collectstatic
    ```

    If there are any updates regarding static files, this step ensures they are collected and served correctly.

## Enabling HTTPS Connection

To secure your Django profile project with HTTPS, follow these steps:

### 1. Setup DNS
Before enabling HTTPS, you need to configure DNS settings for your domain. Follow the instructions provided in the [DigitalOcean DNS Quickstart Guide](https://docs.digitalocean.com/products/networking/dns/getting-started/quickstart/) and [DNS Registrar Guide](https://docs.digitalocean.com/products/networking/dns/getting-started/dns-registrars/) to set up DNS for your domain.

### 2. Create Nginx Server Block
After configuring DNS, set up an Nginx server block to handle HTTPS connections. Refer to Step 5 of the [How To Install Nginx on Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-22-04#step-5-%E2%80%93-setting-up-server-blocks-(recommended)) tutorial to create and configure a server block for your domain.

Make sure not to include the following configuration block to avoid conflicts with the `gunicorn.sock` path:
```nginx
location / {
    try_files $uri $uri/ =404;
}
```

### 3. Secure Nginx with Let's Encrypt
Once your server block is configured, secure Nginx with Let's Encrypt to enable HTTPS encryption. Follow the steps outlined in the [How To Secure Nginx with Let's Encrypt on Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-22-04) tutorial to obtain and install SSL/TLS certificates for your domain.

By completing these steps, you'll have successfully enabled HTTPS connection for your Django profile project, ensuring secure communication between your server and clients.

## Additional Notes

- Replace placeholder text and images with your own content.
- Customize the design and layout to suit your preferences.
- Regularly update the content to reflect your latest achievements and projects.

## Author

[Koyo Nakayama](https://github.com/koyonkym)

## License

This project is licensed under the [MIT License](LICENSE).