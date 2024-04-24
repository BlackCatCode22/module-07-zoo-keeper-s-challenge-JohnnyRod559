def write_zoo_population(output_file_path, hyenas, lions, bears, tigers):
    with open(output_file_path, "w") as output_file:
        output_file.write("Zookeeper's Challenge Zoo Population\n\n")

        # Write Hyena Habitat
        output_file.write("Hyena Habitat:\n\n")
        for hyena in hyenas:
            output_file.write(hyena.animal_id + ", " + hyena.name + "; birthdate: " + str(hyena.birth_date) + "; " + hyena.color +
                              "; " + hyena.sex + "; " + hyena.weight + "; " + hyena.originating_zoo + "; arrived: " +
                              str(hyena.date_arrival) + "\n")
        output_file.write("\n")

        # Write Lion Habitat
        output_file.write("Lion Habitat:\n\n")
        for lion in lions:
            output_file.write(lion.animal_id + ", " + lion.name + "; birthdate: " + str(lion.birth_date) + "; " + lion.color +
                              "; " + lion.sex + "; " + lion.weight + "; " + lion.originating_zoo + "; arrived: " +
                              str(lion.date_arrival) + "\n")
        output_file.write("\n")

        # Write Bear Habitat
        output_file.write("Bear Habitat:\n\n")
        for bear in bears:
            output_file.write(bear.animal_id + ", " + bear.name + "; birthdate: " + str(bear.birth_date) + "; " + bear.color +
                              "; " + bear.sex + "; " + bear.weight + "; " + bear.originating_zoo + "; arrived: " +
                              str(bear.date_arrival) + "\n")
        output_file.write("\n")

        # Write Tiger Habitat
        output_file.write("Tiger Habitat:\n\n")
        for tiger in tigers:
            output_file.write(tiger.animal_id + ", " + tiger.name + "; birthdate: " + str(tiger.birth_date) + "; " + tiger.color +
                              "; " + tiger.sex + "; " + tiger.weight + "; " + tiger.originating_zoo + "; arrived: " +
                              str(tiger.date_arrival) + "\n")
