import udar

def phoneticize(self, approach='safe', guess=False):
        """Return str of running text with stress marked.
        approach  (Applies only to words in the lexicon.)
            safe   -- Only add stress if it is unambiguous.
            freq   -- lemma+reading > lemma > reading
            random -- Randomly choose between specified stress positions.
            all    -- Add stress to all possible specified stress positions.
        guess
            Applies only to out-of-lexicon words. Makes an "intelligent" guess.
        """
        out_text = []
        for tok in self.Toks:
            stresses = tok.stresses()
            if stresses is None:
                if guess:
                    return self.guess_syllable()
                else:
                    out_text.append(tok.orig)
            elif len(stresses) == 1:
                out_text.append(stresses.pop())
            else:
                if approach == 'safe':
                    out_text.append(tok.orig)
                elif approach == 'random':
                    out_text.append(choice(list(stresses)))
                elif approach == 'freq':
                    raise NotImplementedError
                elif approach == 'all':
                    raise NotImplementedError
                else:
                    raise NotImplementedError

        # Create FST
        for word in out_text:
            # append qualifier based on analyzer readings
            # lookup word in fst
            
        return self.respace(out_text)
