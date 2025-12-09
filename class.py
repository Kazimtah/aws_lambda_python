{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "12bd60bb",
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
   "execution_count": 5,
   "id": "ce3872f2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class '__main__.Car'>\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "my_car = Car()\n",
    "print(type(my_car))\n",
    "print(isinstance(my_car, Car))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9c62a85c",
   "metadata": {},
   "outputs": [],
   "source": []
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
