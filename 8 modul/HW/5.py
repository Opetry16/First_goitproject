import random

participants = {
    "603d2cec9993c627f0982404": "test@test.com",
    "603f79022922882d30dd7bb6": "test11@test.com",
    "60577ce4b536f8259cc225d2": "test2@test.com",
    "605884760742316c07eae603": "vitanlhouse@gmail.com",
    "605b89080c318d66862db390": "elhe2013@gmail.com",
}

def get_random_winners(quantity, participants):
    if quantity > len(participants):
        return []
    participants_id = list (participants.keys())
    random.shuffle (participants_id)
    winners = random.sample (participants_id, k=quantity)
    result = [participants[participant_id] for participant_id in winners]
    return result