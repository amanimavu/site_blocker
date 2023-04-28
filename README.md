# Site Blocker

This python program meant to automate the task
of blocking the browser from accessing certain
websites. These sites that distract you when
you want to be productive on your computer or
explicit sites that you want to protect your
children or yourself from accessing.<br>

# How it works

It works by maanipulating the file in your
system that maps domain names to their respective
IP addresses(i.e hosts file in Ubuntu linux).
To block the selected sites, the program includes
a pair of domain names paired with the IP address
of localhost(in this format: ``127.0.0.1    <domain name>``).
That way the domain names are redirected to the IP
address of localhost thus blocking the browser from
accessing the site.<>
