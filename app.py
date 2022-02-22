

import streamlit as st

from wordler.utils import submit_guesses, print_letters_hints, is_valid_word, keep_valid_guesses, convert_guess_and_hints, get_logo
from wordler.solver import Wordler

get_logo()

st.sidebar.title("WORDLEr")
st.sidebar.caption("A [WORDLE](https://www.nytimes.com/games/wordle/index.html) ch🟨🟩t sh🟨🟨t made by [Siavash Yasini](https://www.linkedin.com/in/siavash-yasini/).")
st.markdown("""
1. Type in the 5️⃣ letters for your GUESS in each step (Start with **_ARISE_**! Trust me...). 
2. Select the colors you get back from [WORDLE](https://www.nytimes.com/games/wordle/index.html) for each letter, 
3. Press 'submit' to get the top suggestions for next guess.
4. Use the 👈 sidebar to change the settings.
5. Share this app with your friends! 
""")

st.sidebar.header("Settings")

n_steps = st.sidebar.slider("Number of steps", 1, 10, value=3)
n_suggestions = st.sidebar.slider("Suggestion List Limit (0 shows all)", 0, 30, value=10,)
metric = st.sidebar.selectbox("suggestion metric:", ["wiki score", "letter score", "wiki score x letter score"])

all_guesses, all_hints = submit_guesses(n_steps)
valid_guesses, valid_hints = keep_valid_guesses(all_guesses, all_hints)


st.sidebar.markdown("---")
if valid_guesses:
    st.sidebar.header("Hints")
print_letters_hints(valid_guesses, all_hints)
for guess in valid_guesses:
    is_valid_word(guess)

# Let the maginc happen...
wordler = Wordler()
for guess, hint in zip(valid_guesses, valid_hints):
    wordler.update_constraint(*convert_guess_and_hints(guess, hint))

if st.session_state["FormSubmitter:form-submit"]:
    st.header("Next Word Suggestions")
    st.dataframe(wordler.suggest_next_word(key_sort=metric, head=n_suggestions))

st.sidebar.markdown("---")

st.sidebar.info("""
Note on metrics:\n
Words with more frequent letters have a higher '**letter score**' (suggested for 1st or 2nd guesses).\n

More frequent words have a higher '**wiki score**' (suggested for later guesses). 

""")