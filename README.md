# Earth Elevation Action
An action that takes in a collection of latitude and longitude values and outputs the corresponding elevations at those locations.

## Example Usage
```
steps:
  - name: Run the Action
    id: action-with-output
    uses: krolldevelopment/EarthElevationAction@main
    with:
      coordinatesJSON: '[{"latitude": 40.748817, "longitude": -73.985428}, {"latitude": 35.748817, "longitude": -78.985428}, {"latitude": 37.774929, "longitude": -122.419416}]'
  - name: Use the output
    run: |
      echo "Elevations output ${{ steps.action-with-output.outputs.elevationsJSON }}"
```
