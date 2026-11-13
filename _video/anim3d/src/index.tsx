import React from "react";
import { Composition, registerRoot } from "remotion";
import { PhoDemo, PHO_FRAMES } from "./videos/pho/Pho";
import { VangVideo, VANG_FRAMES } from "./videos/vang/Vang";
import { Bia } from "./videos/vang/Bia";
const Root: React.FC = () => <>
  <Composition id="PhoDemo" component={PhoDemo} durationInFrames={PHO_FRAMES} fps={30} width={1920} height={1080} />
  <Composition id="Vang" component={VangVideo} durationInFrames={VANG_FRAMES} fps={30} width={1920} height={1080} />
  <Composition id="Bia" component={Bia} durationInFrames={1} fps={30} width={1920} height={1080} />
</>;
registerRoot(Root);
