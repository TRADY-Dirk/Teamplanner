class Person:
    def __init__(self, name="New Member", picture="default.png", uid=0):
        self.uid = uid
        self.name = name
        self.picture = picture
        self.skillset = {
            "organize": False,
            "realize": False,
            "perfection": False,
            "coordination": False,
            "teamplay": False,
            "communication": False,
            "renew": False,
            "specialize": False,
            "observe": False
        }

    def toggleSkill(self, skillname):
        self.skillset[skillname] = not bool(self.skillset[skillname])
        return self.skillset[skillname]
