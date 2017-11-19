# Function to parse an input file with data, that is too big to be uploaded in 1 go
# Divides the file into several smaller pieces, that you can then upload to MySQL
def subdivide_file(filename, max_entries_per_file):
    print("\nParsing file {0}".format(filename))
    # Open the input file
    inputfile = open(filename)

    filename = filename[0:-4] # remove the ".csv" extension
    print(filename)

    output_string = ""
    line_counter = 0
    subfile_counter = 1
    # For each line (with point data) in the file do:
    for line in inputfile:
        # Add line to output
        output_string += line
        line_counter += 1

        if (line_counter == max_entries_per_file):

            output_filename = filename + "_part_" + str(subfile_counter) + ".csv"
            output_file = open(output_filename, "w")
            output_file.write(output_string)
            output_file.close()

            line_counter = 0 # reset line counter
            subfile_counter += 1 # increase the number of the subfile
            output_string = "" # empty the buffer

    if (line_counter != 0):

        output_filename = filename + "_part_" + str(subfile_counter) + ".csv"
        output_file = open(output_filename, "w")
        output_file.write(output_string)
        output_file.close()

        line_counter = 0 # reset line counter
        subfile_counter += 1 # increase the number of the subfile
        output_string = "" # empty the buffer


    return 0

max_entries_per_file = 50000
subdivide_file("input_data.csv", max_entries_per_file)
