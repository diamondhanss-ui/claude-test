# Product lens
Score: 3/10 | Vote: FUND IF

## What is strong
- The one-sentence pitch is already clear: tell a chat bot what you want, get the cheapest fares ranked. It passes the one-sentence test.
- Chat is a low-friction entry point. There is no app to install and no form to fill in, which suits the first five minutes.
- The audience is specific: flexible leisure travelers who can move their dates. Flexibility is what makes "cheapest over the next few months" a real job.

## What would kill it (the top 3, most dangerous first)
1. **No one thing done brilliantly.** "A wrapper around an LLM" describes the plumbing, not the experience. The brief does not say what the user gets that Google Flights or a price-alert tool does not already give them. The Product lens asks what to cut until one thing remains; right now the brief does not name it.
2. **The experience is handed between systems, and the data source is undecided.** A ranked list that is stale, wrong or unbookable breaks the product at the seam between the LLM, the fare data and the airline or seller site. The brief names no flight-data provider and no booking hand-off. The Product lens treats the whole path, from the chat message to the ticket, as the product.
3. **The first five minutes are undefined, and the promise is unproven.** The brief does not say what the traveler sees after typing a request, how a vague request ("somewhere warm in March") gets clarified, or how the bot shows its answer is correct. An LLM that confidently names a wrong fare destroys trust at once, and this is the part the user cannot see. Nothing in the brief says how it will be checked.

## The questions I would ask the founder
- In one sentence, what does this do that a fare-search site cannot? Which single thing would you keep if you had to cut everything else?
- Walk me through the first five minutes: the exact message, the exact reply, and the moment the user decides it was worth it.
- Where does a fare come from, and how fresh is it? What happens when the price has changed by the time they click? (Open question: no provider or data cost is known. /founder-cfo answers the cost side.)
- What do people use today for this, and what do they complain about? (Open question. /founder-competitors answers it.)
- Would flexible travelers return to a chat bot, or use it once? How many say they would, and what would flip a no? (Open question. /founder-consumer answers it.)
- Which chat platform first, and why only that one? (Open question: the brief lists three.)

## If FUND IF: the conditions
- Name the one thing in a single sentence, and cut anything that does not serve it (start with one chat platform, not three).
- Choose a real flight-data source and show the bot's answers match what the seller site shows, with the price and the date of the check visible in each reply.
- Define the end-to-end path through to a bookable link, and the failure behavior when a fare is stale or missing.
- Show that real users, not only simulated ones, prefer the result to existing tools. Run /founder-competitors and /founder-consumer first, and /founder-cfo for data and LLM running costs, since a free tool still has them.
