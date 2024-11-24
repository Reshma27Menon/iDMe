{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e5c6eeb5-2f25-4402-a141-5928d3003d2f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import json"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "edbf7d3e-05ef-4b31-8dc3-bd077f8fc279",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = [\n",
    "    {\n",
    "        \"name\": \"0000\",\n",
    "        \"location\": [\n",
    "            \"/store/group/lpcmetx/iDMe/Samples/Ntuples/background/2018/DY/DYJetsToLL/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/crab_iDMe_DYJetsToLL_2023_03_29-10_24/230329_152459/0002/\"\n",
    "        ],\n",
    "        \"sum_wgt\": 1063708.0,\n",
    "        \"type\": \"bkg\",\n",
    "        \"year\": 2018,\n",
    "        \"xsec\": 5379000.0,\n",
    "        \"nFiles\": 1007,\n",
    "        \"blacklist\": []\n",
    "    }\n",
    "]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "6488576d-70b7-4deb-844d-0360696e40f9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Write to a JSON file\n",
    "with open('datasets.json', 'w') as json_file:\n",
    "    json.dump(data, json_file, indent=4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b497e026-468a-44b4-acf7-adf984e91489",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
