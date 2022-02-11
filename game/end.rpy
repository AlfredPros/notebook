label end:
    if goodend == 1:
        T "I see your condition has improved."
        MC "Is that so?"
        T "Yeah, I can see that both mentally, and physically you're getting better."
        MC "That's good."
        T "I'll still to have ask you to take this pill everyday."
        MC "I understand, thankyou."
        T "You're welcome."
        window hide
        pause 2
        show text "{size=56}Good End{/size}" with Dissolve(1)
        pause
        
    else:
        T "His condition is worsen, I'm not quite sure what happened."
        if dogdie == 1:
            T "I think when his pet died it made him completely snapped."
        else:
            T "I think when his pet ran away it made him completely snapped."
        T "He began to feed his 'dog' when he isn't there anymore"
        T "It's difficult to get him to take the pills, and his schizophrenia is getting worse."
        T "Now, what should I do."
        window hide
        pause 2
        show text "{size=56}Bad End{/size}" with Dissolve(1)
    pause
    hide text with Dissolve(0.8)
    pause 2
    return
