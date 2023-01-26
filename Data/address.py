import csv

# Open the input file and read the data
with open("input.txt", "r") as input_file:
    reader = csv.DictReader(input_file)

    # Open the output file and write the reformatted data
    with open("output.txt", "w", newline="") as output_file:
        fieldnames = ["Name","Add_Number", "StreetName", "Zip_Code", "County", "State", "Longitude", "Latitude", "Addr_Type"]
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            # Extract the columns we want to keep
            add_number = row["Add_Number"]
            street_name = row["StreetName"].lower()
            zip_code = row["Zip_Code"]
            county = row["County"]
            state = row["State"]
            longitude = row["Longitude"]
            latitude = row["Latitude"]
            addr_type = row["Addr_Type"]
            
            #Create new "Name" column from  "Add_Number"."StreetName"."Zip_Code"
            name = f"{add_number}{street_name}.{zip_code}".lower()
            
            # Write the reformatted data to the output file
            writer.writerow({
                "Name": name,
                "Add_Number": add_number,
                "StreetName": street_name,
                "Zip_Code": zip_code,
                "County": county,
                "State": state,
                "Longitude": longitude,
                "Latitude": latitude,
                "Addr_Type":addr_type
            })
