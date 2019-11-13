# Enterodump

Script for downloading FASTA files from [Enterobase](http://enterobase.warwick.ac.uk) using barcodes.
Takes a list of barcodes in a file called barcode_list.txt (see example.txt) and downloads the files to the download/-subdirectory of the scripts path.

### Note

Requires a valid API-Token from Enterobase.
You can request one [here](https://enterobase.readthedocs.io/en/latest/api/api-getting-started.html).

## Usage

```python enterodump.py -d <DATABASE> -t <API-TOKEN>```

## Example

```python enterodump.py -d clostridium -t eyJhbGciOiJIUzI1NiIsImV4cCI6MTU4OTQwODI5Miwia...```

## Output

```
Downloading FASTA for barcode CLO_AA0229AA_AS... done.
Downloading FASTA for barcode CLO_AA0230AA_AS... done.
Downloading FASTA for barcode CLO_AA0234AA_AS... done.
```