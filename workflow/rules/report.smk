"""A small, reproducible starter rule. Replace it with the first real stage."""


rule render_report:
    input:
        config["example_input"]
    output:
        config["report"]
    log:
        "logs/render_report.log"
    params:
        project_name=config["project_name"]
    conda:
        "../envs/base.yaml"
    shell:
        r"""
        mkdir -p "$(dirname {output:q})"
        {{
          printf 'Project: %s\\n' {params.project_name:q}
          printf '\\nInput:\\n'
          cat {input:q}
        }} > {output:q} 2> {log:q}
        """
