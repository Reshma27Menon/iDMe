{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b7b3b3e9-0ab9-4d33-86de-432efee75487",
   "metadata": {},
   "outputs": [],
   "source": [
    "import json"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "479a5be5-ecf6-445a-afe9-e5f739fbfd76",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = [\n",
    "    {\n",
    "        \"name\": \"0000\",\n",
    "        \"location\": [\n",
    "            \"\"\n",
    "        ],\n",
    "        \n",
    "        \"type\": \"bkg\",\n",
    "        \"year\": 2022,\n",
    "        \"xsec\": 10\n",
    "        \n",
    "    }\n",
    "]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "b151f95c-03a6-4c7a-a8f2-f2add79442c2",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('2022.json', 'w') as json_file:\n",
    "    json.dump(data, json_file, indent=4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a46a31af-3550-49e5-ac4f-0e74f3ecd9e8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:coffea]",
   "language": "python",
   "name": "conda-env-coffea-py"
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
   "version": "3.8.17"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
