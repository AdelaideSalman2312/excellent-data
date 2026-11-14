#Day 004 :Preparing Data

A Kaggle data set does not prepare you for the real world messy data .
Real world data is messy . Before we give it to a machine learning model , we first need to understand what we are working with .

**Imagine getting employee data from different systems**
One system says :



Another says:






To a human , they mean the same thing . To a computer, they're not automatically the same . We have :

- different columns 
- different formats
- different values representing the sane thing

But before using this kind of data we need to make it consistent .

Then we get to the part where information is genuinely missing. Never assume - as I this imagine me on top of the buildings the way Shontelle sang shouting from the rooftops : Never assume : Now we have should have a listicle of questions why is information missing because :
 - someone may have forgot to enter it .
 - the system didn’t collect it?
 - the information genuinely is not available 


Those situations might all look like an empty cell. But they can mean very different things.

- So what do we do?

- Remove the row?

- Estimate the value?

- Leave it as missing?

There isn’t one answer. First, we need to understand why it’s missing.

**Then there are outliers**

Imagine you're looking at salaries:

Employee                   salary
Alex                        ksh850,000
Sam                         ksh920,000
Maya                        ksh1,120,000
Chris                       ksh11,000,000

Paaaaaaaaaauuuuuuuuuuuussssssssssssssseeeeeeeeeeeeeeeee!!!!!!

That last value is very different from the rest. We call that an **outlier**.

But here’s something important:

An outlier isn’t automatically bad data.

Maybe someone accidentally added an extra zero. Or maybe Chris is actually the CEO.

The value is unusual. But unusual doesn’t always mean wrong. So before removing an outlier, we need to ask:

**Is this an error?**

Or:

**Is this something important that really happened?**

*Welcome - and have a seat the real AI work has just began**

In my head i always pictured ,machine learning as follows :

Data -> Model -> Prediction 

But the reality is as follows :

Collect → Understand → Clean → Transform → Model → Evaluate

Before the model even starts learning, someone has to understand the data.

And sometimes, that takes more work than training the model itself.

# Back to my favourite website (JKC)

Imagine building a RAG to understand customer reviews.
Data contains:

Great service!

GREAT SERVICE!!!

gr8 service

And maybe one review is:

GREEEEAAAAATTTTTT!!! 🤩🔥🔥🔥

Does that automatically mean that it is bad data?

Not necessarily.

But it may need to be handled differently depending on what we’re trying to do. This is why data preparation isn’t just about making everything look neat. It’s about understanding the information well enough to decide what should happen next.

**Welcome to data analysis : are you still trying to find the "Clean Data" button .**
Every small decision affects how the model learns .
If we :
- fill missing values incorrectly, we might create false patterns
- remove too much data, we might lose useful information
- delete every unusual value, we might remove important real-world events

So data preparation isn’t simply:
about having a perfectly clean CSV or a perfect spreadsheet.

It about asking the right questions:

- What does this data actually represent?

- What’s missing?

- What’s inconsistent?

- What’s unusual?

- And is that unusual thing an error—or a signal?

Something very useful to pick is that  understanding the business is part of data preparation : You cannot walk into a bakery business and expect it to work the same as real estate . 

And a more advanced model can’t automatically fix data we don’t understand.



















