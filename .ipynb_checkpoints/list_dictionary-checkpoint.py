{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "94beb8a9",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-2-4c059b538da6>, line 34)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-2-4c059b538da6>\"\u001b[0;36m, line \u001b[0;32m34\u001b[0m\n\u001b[0;31m    \"Instance_id\" = \"i-05gfke64k30jk\"\u001b[0m\n\u001b[0m                  ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "colors = [\"Red\",\"Orange\", \"Yello\", \"Green\", \"Blue\", \"Indigo\", \"Violet\"]\n",
    "capacities = [10000, 12000, 9000, 8000, 10000, 11000, 9000]\n",
    "\n",
    "#Operation of the list on python3\n",
    "print(sum(capacities)/len(capacities))\n",
    "capacities.append(12000)\n",
    "capacities.insert(0,10000)\n",
    "capacities.remove(9000)\n",
    "print(colors.index('Blue'))\n",
    "print('Red' in colors)\n",
    "print('Red' not in colors)\n",
    "\n",
    "\n",
    "# accessing the index of the list and add a new item to the list on a specific index\n",
    "\n",
    "colors[0] = \"Bright Red\"\n",
    "print(colors[0])\n",
    "print(capacities[1])\n",
    "\n",
    "\n",
    "#slice of a list on python language programe:list[from:to:step]\n",
    "print(colors[:])\n",
    "print(colors[2:])\n",
    "print(colors[:3])\n",
    "print(colors[-4:])\n",
    "\n",
    "print(colors[::-1])\n",
    "print(colors[::2])\n",
    "\n",
    "# dictionary type in python lanauges others language it might a map type\n",
    "\n",
    "info = {\n",
    "    \n",
    "    \"Instance_id\" = \"i-05gfke64k30jk\",\n",
    "    \"Instance_type\" = \"m5.large\",\n",
    "    \"Image_id\" = \"id25555-kkkak-all12233\"\n",
    "    \n",
    "}\n",
    "\n",
    "info[\"ExtraInfo\"] = 'This is extra info'\n",
    "print(info(\"ImageId\"))\n",
    "\n",
    "\n",
    "del info[\"Instance_type\"] \n",
    "print('ExtraInfo' in info) #True \n",
    "print('EExtraInfo'not in info)  # False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0ad2df5c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5e9cb26b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "42b386b4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c4ca396c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "870cec58",
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
