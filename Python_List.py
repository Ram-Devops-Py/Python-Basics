{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['India', 'United Kingdom', 'United States', 'Australia', 'New Zealand']\n"
     ]
    }
   ],
   "source": [
    "#Print the list\n",
    "Countries = ['India','United Kingdom','United States','Australia','New Zealand']\n",
    "print(Countries)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['India', 'United Kingdom', 'UAE', 'Australia', 'New Zealand']\n"
     ]
    }
   ],
   "source": [
    "# Replace the US with UAE using index value\n",
    "Countries[2] = 'UAE'\n",
    "print(Countries)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['India', 'United Kingdom', 'UAE', 'Australia', 'New Zealand', 'South Africa', 'South Africa', 'South Africa', 'South Africa', 'SouthAfrica', 'South Africa']\n"
     ]
    }
   ],
   "source": [
    "#Add SA to the existing list\n",
    "Countries.append('South Africa')\n",
    "print(Countries)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "11\n"
     ]
    }
   ],
   "source": [
    "Length_of_list = len(Countries)\n",
    "print(Length_of_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['India', 'United Kingdom', 'UAE', 'Australia', 'New Zealand']\n",
      "['South Africa', 'South Africa', 'South Africa', 'South Africa', 'SouthAfrica']\n"
     ]
    }
   ],
   "source": [
    "#Print selected values using index range\n",
    "print(Countries[0:5])\n",
    "print(Countries[5:10])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['India', 'United Kingdom', 'UAE', 'Australia', 'New Zealand', 'South Africa', 'South Africa', 'South Africa', 'SouthAfrica', 'South Africa']\n"
     ]
    }
   ],
   "source": [
    "#Remove a value from list using remove() function\n",
    "Countries.remove(\"South Africa\")\n",
    "print(Countries)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['India', 'United Kingdom', 'UAE', 'Australia', 'New Zealand', 'South Africa', 'South Africa', 'South Africa']\n"
     ]
    }
   ],
   "source": [
    "#Remove a value from list using pop() function\n",
    "poped_Countries = Countries.pop()\n",
    "print(Countries)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
