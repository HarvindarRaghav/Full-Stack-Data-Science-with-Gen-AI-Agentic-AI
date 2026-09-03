{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1a86ad80",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'streamlit'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mModuleNotFoundError\u001b[39m                       Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m streamlit \u001b[38;5;28;01mas\u001b[39;00m st\n",
      "\u001b[31mModuleNotFoundError\u001b[39m: No module named 'streamlit'"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dc055083",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'streamlit'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mModuleNotFoundError\u001b[39m                       Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[1]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m streamlit \u001b[38;5;28;01mas\u001b[39;00m st\n\u001b[32m      2\u001b[39m \n\u001b[32m      3\u001b[39m \u001b[38;5;66;03m# 1. Add a title\u001b[39;00m\n\u001b[32m      4\u001b[39m st.title(\u001b[33m\"My First Streamlit App created by PRAKASH SENAPATI\"\u001b[39m)\n",
      "\u001b[31mModuleNotFoundError\u001b[39m: No module named 'streamlit'"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "\n",
    "# 1. Add a title\n",
    "st.title(\"My First Streamlit App created by PRAKASH SENAPATI\")\n",
    "\n",
    "# 2. Add some text\n",
    "st.write(\"Welcome! This app calculates the square of a number.\")\n",
    "\n",
    "# 3. Create an interactive slider\n",
    "st.header(\"Select a Number\")\n",
    "\n",
    "number = st.slider(\"Pick a number\", 0, 5, 0)\n",
    "\n",
    "# 4. Calculate and display the result\n",
    "st.subheader(\"Result\")\n",
    "\n",
    "squared_number = number * number\n",
    "\n",
    "st.write(f\"The square of **{number}** is **{squared_number}**.\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": ".venv (3.11.4.final.0)",
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
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
