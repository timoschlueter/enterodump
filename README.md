# Enterodump

Script for downloading FASTA files from [Enterobase](http://enterobase.warwick.ac.uk) using assembly barcodes.
Takes a list of assembly barcodes in a file (see example.txt) and downloads the files to the download/-subdirectory of the scripts path.

### Note

Requires a valid API-Token from Enterobase.
You can request one [here](https://enterobase.readthedocs.io/en/latest/api/api-getting-started.html).

## Usage

```python enterodump.py -d <DATABASE> -l <TEXTFILE> -t <API-TOKEN>```

## Example

```python enterodump.py -d clostridium -l example.txt -t eyJhbGciOiJIUzI1NiIsImV4cCI6MTU4OTQwODI5Miwia...```

## Output

```
Downloading FASTA for barcode CLO_AA0229AA_AS... done.
Downloading FASTA for barcode CLO_AA0230AA_AS... done.
Downloading FASTA for barcode CLO_AA0234AA_AS... done.
```