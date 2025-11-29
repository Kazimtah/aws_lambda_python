{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2f456a6a",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "EOL while scanning string literal (<ipython-input-1-e51536fec7c9>, line 20)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-1-e51536fec7c9>\"\u001b[0;36m, line \u001b[0;32m20\u001b[0m\n\u001b[0;31m    print(f\" I am thinking of a random country from the list {country_keys_string}. Guess the 2025 population of this country\u001b[0m\n\u001b[0m                                                                                                                             ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m EOL while scanning string literal\n"
     ]
    }
   ],
   "source": [
    "import random \n",
    "TOTAL_GUESS = 2\n",
    "\n",
    "POPULATION_DICT = {\n",
    "    'USA': 331,\n",
    "    'CHINA': 1439,\n",
    "    'India': 1380,\n",
    "    'Brazil': 212\n",
    "}\n",
    "\n",
    "def main():\n",
    "    print(\"Hello and Wellcome to the guesing game!\")\n",
    "    start_game()\n",
    "    \n",
    "def start_game():\n",
    "    country_keys = list(POPULATION_DIC.keys())\n",
    "    country_keys_string = \", \" .join(country_keys)\n",
    "    random_country_key =  random.choice(country_keys)\n",
    "    \n",
    "    print(f\" I am thinking of a random country from the list {country_keys_string}. Guess the 2025 population of this country\n",
    "           {TOTAL_GUESS} times. I will tell you so high\")\n",
    "          \n",
    "for gues_count in range(TOTAL_GUESS):\n",
    "          print(f\" You have {TOTAL_GUESS - gues_count} guesses remaining.\")\n",
    "          process_user_guess(random_country_key)\n",
    "          \n",
    "while True:\n",
    "          guess_country = input(\"What country am I thinking of?\")\n",
    "          if guess_country not in country_keys:\n",
    "              print(\"That country is not list \")\n",
    "          else: \n",
    "              break\n",
    "          \n",
    "#checking the guesss\n",
    "if guess_country == random_country_key:\n",
    "          print(\"Your gussed is true\")\n",
    "def process_user_guess(random_country_key):\n",
    "          gues_population = int(input(\"Guess the population of the country in a million\"))\n",
    "          \n",
    "          if gues_population == \"\" or not gues_population.isnumeric():\n",
    "              print(\"This is not a number\")\n",
    "          elif int(gues_population) == POPULATION_DICT[random_country_key]:\n",
    "              print(f\"{ues_population} million is the exact population\")\n",
    "          elif int(gues_population) < POPULATION_DICT[random_country_key]:\n",
    "              print(f\"{gues_population} is not in the guesss population \")\n",
    "          else:\n",
    "              print(f\"{gues_population} million is to high\")\n",
    "          print()\n",
    "main()\n",
    "          "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "614d9193",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "63153012",
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
