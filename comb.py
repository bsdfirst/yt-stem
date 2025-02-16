#!/usr/bin/env python3

import itertools

inst = [
  'BASS',
  'DRUMS',
  'GUITAR',
  'PIANO',
  'VOCALS',
  'OTHER',
]

for i in range( 2, 6 ):
  #print( list( itertools.combinations( inst, i ) ) )

  for cb in list( itertools.combinations( inst, i ) ):
    outstr='_'.join( cb )
    instr=' '.join( [ f'-i ${{p}}/{s.lower()}.mp3' for s in cb ] )


    print( f'ffmpeg {instr} -filter_complex amix=inputs={len(cb)}:${{filter}} "${{out_path}}/${{TITLE}} [1.00x__{outstr}].mp3"' )

#ffmpeg -i ${p}/bass.mp3 -i ${p}/drums.mp3 -i ${p}/guitar.mp3 -i ${p}/piano.mp3 -i ${p}/vocals.mp3 -filter_complex amix=inputs=4:${filter} "${out_path}/${TITLE} [1.00x__NO_OTHER].mp3"
