#!/usr/bin/env nextflow

nextflow.enable.dsl = 2 

ch_numba_py = file("${projectDir}/bin/numba_test.py")

process numba_test {
    container 'quay.io/parsboy1987/python_slim:v2'

    input:
    path ch_numba_py 

    script:
    """
    python ${ch_numba_py}
    """
}

workflow {
    numba_test(ch_numba_py) 
}
