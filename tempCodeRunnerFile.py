            print(B)
            print(setXValues(B))
            clear(window)
            window.update()
            for thing in B:
                print(thing)
            for thing in B:
                thing.draw(window)
                window.update()
                time.sleep(.5)