{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "568acc6a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Red\n",
      "Orange\n",
      "Yellow\n",
      "Green\n",
      "Blue\n",
      "Indigo\n",
      "Violet\n",
      "Red\n",
      "*******************\n",
      "Red ff0000\n",
      "Green\n",
      "*******************\n",
      "Green 08000\n",
      "Blue\n",
      "*******************\n",
      "Blue 0000ff\n"
     ]
    }
   ],
   "source": [
    "colors = ['Red','Orange', \"Yellow\", 'Green', \"Blue\", 'Indigo', 'Violet']\n",
    "for c in colors:\n",
    "    print(c)\n",
    "    \n",
    "colors_values = {'Red': 'ff0000', 'Green': '08000', 'Blue': '0000ff'}\n",
    "\n",
    "for k in colors_values: \n",
    "    print(k)\n",
    "    print(\"*******************\")\n",
    "    print(k, colors_values[k])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c6fad25d",
   "metadata": {},
   "outputs": [],
   "source": [
    "connected = False\n",
    "attempts = 0\n",
    "while not connected and attempts < MAX_ATTEMPTS:\n",
    "    attempts +=1\n",
    "    print(f\"connecting attemp {attempts}.\")\n",
    "    connected = attempt_connect()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "34da4adf",
   "metadata": {},
   "outputs": [],
   "source": [
    "print([c.upper() for c in colors])\n",
    "print([c for c in colors if c.startwith('G')])"
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
