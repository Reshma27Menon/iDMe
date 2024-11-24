{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "009e7cb4-adb3-48c2-b278-7bb4a22f67a6",
   "metadata": {},
   "outputs": [],
   "source": [
    "import json"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "b5632c24-be43-47ad-b0c8-1227ec70f128",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = [\n",
    "    {\n",
    "        \"name\": \"0000\",\n",
    "        \"location\":\"/uscms/home/reshmar/nobackup/CMSSW_13_0_13/src/iDMe/AODSkimmer/Final_DYJets_2022_output.root\",\n",
    "        \"type\": \"bkg\",\n",
    "        \"year\": 2022,\n",
    "        \"xsec\": 10,\n",
    "        \"nFile\": 1,\n",
    "        \"blacklist\":[]\n",
    "    }\n",
    "]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "733fb43e-5dac-43b6-a4a6-26b61319df4b",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('2022bkgnew.json', 'w') as json_file:\n",
    "    json.dump(data, json_file, indent=4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "183aad72-a855-427e-8fdf-812d502addc6",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3626a774-beff-4fc1-883b-11195f922cc5",
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
