RGVFlood Development Process
============================

.. mermaid:: 

   sequenceDiagram
      participant Alice
      participant Bob
      Alice->John: Hello John, how are you?
      loop Healthcheck
          John->John: Fight against hypochondria
      end
      Note right of John: Rational thoughts <br/>prevail...
      John-->Alice: Great!
      John->Bob: How about you?
      Bob-->John: Jolly good!
.. 
    gantt
        dateFormat  YYYY-MM-DD
        title RGVFlood Development Plan
        excludes weekends

        section Regional Hydrology and Hydraulics

        section Real Time Hydrologic Systems Network

        section Cyberinfrastructure
