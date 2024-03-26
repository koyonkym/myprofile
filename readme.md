# My Profile

This is a README.md file for the **My Profile Project**.

## Overview

This project serves as my personal profile website, showcasing my skills, background, and achievements.

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

### Configuration Note

Depending on your project structure, you may need to configure the Nginx `location` block for serving static files differently. If your static files are located in a subdirectory within the project directory, you should use the `alias` directive instead of the `root` directive.

Example:

```nginx
location /static/ {
    alias /home/sammy/myprofile/static/;
}
```

This ensures that Nginx correctly serves static files from the specified directory.

## Additional Notes

- Replace placeholder text and images with your own content.
- Customize the design and layout to suit your preferences.
- Regularly update the content to reflect your latest achievements and projects.

## Author

[Koyo Nakayama](https://github.com/koyonkym)

## License

This project is licensed under the [MIT License](LICENSE).