{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "c657ccb6",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Car:\n",
    "    def move(self):\n",
    "        print(\"car is moving\")\n",
    "    def stop(self):\n",
    "        print(\"Car is stopping\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "427b2d60",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class '__main__.Car'>\n",
      "True\n",
      "car is moving\n",
      "None\n",
      "Car is stopping\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "my_car = Car()\n",
    "print(type(my_car))\n",
    "print(isinstance(my_car, Car))\n",
    "print(my_car.move())\n",
    "print(my_car.stop())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "07fc819a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Usename: Kazim, Group: leiriehrie, shell: /bin/bash\n"
     ]
    }
   ],
   "source": [
    "class Linuxuser:\n",
    "    def __init__(self, username, password, shell):\n",
    "        self.username = username\n",
    "        self.password = password\n",
    "        self.shell = shell\n",
    "        \n",
    "    def show_user_info(self):\n",
    "        print(f\"Usename: {self.username}, Group: {self.password}, shell: {self.shell}\")\n",
    "\n",
    "linuxuser = Linuxuser(\"Kazim\", \"leiriehrie\", \"/bin/bash\")\n",
    "linuxuser.show_user_info()\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "07703d6a",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Services:\n",
    "    def __init__(self, service_name):\n",
    "        self.service_name\n",
    "        \n",
    "    # Showing the status of the services\n",
    "    def status(self):\n",
    "        print(f\"Status of {self.service_name}\")\n",
    "    #stoping the services on linux operating system\n",
    "    def stop(self):\n",
    "        print(f\"Stopping the {self.service_name}\")\n",
    "    #starting the linux services\n",
    "    def start(self):\n",
    "        print(f\"Starting the {self.service_name}\")\n",
    "services_name = Services(\"apache2\")\n",
    "services_name.status()\n",
    "services_name.stop()\n",
    "services_name.start()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
