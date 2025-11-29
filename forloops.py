{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "64a0808c",
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
      "Red ff0000\n",
      "Green\n",
      "Green 08000\n",
      "Blue\n",
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
    "    print(k, colors_values[k])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cc3df420",
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
