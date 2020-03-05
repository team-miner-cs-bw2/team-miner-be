### RUN THIS IF YOU DONT HAVE A NAME YET

            # # Change name if not already done.
            # if self.name_changed == False and self.gold <= 1000:
            #     self.rand_room()
            # # Do every loop:
            # # Sell treasure.
            # if self.encumbered and self.places['shop']['room_id'] or self.encumbrance >= 5:
            #     self.sell_things()
            #     self.minimum_gold = True

            # if self.gold >= 1000 and self.minimum_gold == True:
            #     if not self.name_changed and self.gold >= 1000:
            #         self.name_change()
            #         print("at the name change")

            ### RUN THIS IF YOU HAVE A NAME ALREADY
            if self.places['pirate']['room_id'] and not self.name_changed and self.gold >= 1000:
                self.name_change()
            # Pray at the dash shrine once.
            if self.places['dash']['room_id'] and self.name_changed and not self.dash_:
                self.to_dash()
            # Pray at the flight shrine once.
            if self.places['flight']['room_id'] and self.name_changed and not self.flight:
                self.to_flight()
            # Pray at the warp shrine once.
            if self.places['warp']['room_id'] and self.name_changed and not self.warp:
                self.to_warp()
            # Do every loop:
            # Sell treasure.
            if self.encumbered and self.places['shop']['room_id']:
                self.sell_things()
            # Go to random rooms to collect treasure until you can carry no more.
            if not self.encumbered:
                self.rand_room()
            # Go get a golden snitch.
            if self.encumbered and self.warp_:
                self.dimensional_traveler()
            # Mine lambda a coin.
            if self.encumbered and self.places['well']['room_id'] and self.name_changed:
                self.coin_dash()
